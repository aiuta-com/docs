import React from 'react';
import { createRoot } from 'react-dom/client';
import { AiutaTryOnButton, AiutaTryOnSdkProvider } from "aiuta-try-on-sdk";

// Initialize the SDK when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
  console.log('DOM loaded, initializing Aiuta SDK...');
  initializeAiutaSDK();
});

function initializeAiutaSDK() {
  try {
    // Look for provider elements
    const providers = document.querySelectorAll('aiuta-try-on-sdk-provider');
    console.log('Found providers:', providers.length);
    
    providers.forEach((providerElement, providerIndex) => {
      const apiKey = providerElement.getAttribute('apikey');
      console.log(`Provider ${providerIndex} API key:`, apiKey);
      
      if (!apiKey) {
        console.error('Missing apikey attribute on provider');
        return;
      }
      
      // Find associated button elements
      const buttons = providerElement.querySelectorAll('aiuta-try-on-button');
      console.log(`Found ${buttons.length} buttons in provider ${providerIndex}`);
      
      // Collect all button data
      const buttonData = [];
      buttons.forEach((buttonElement, buttonIndex) => {
        const skuId = buttonElement.getAttribute('skuid');
        const skuCatalogName = buttonElement.getAttribute('skucatalogname') || '';
        const dynamicStylesAttr = buttonElement.getAttribute('dynamicstyles');
        
        console.log(`Button ${buttonIndex} - skuId: ${skuId}, catalog: ${skuCatalogName}`);
        
        if (!skuId) {
          console.error('Missing skuid attribute on button');
          return;
        }
        
        let dynamicStyles = {};
        if (dynamicStylesAttr) {
          try {
            dynamicStyles = JSON.parse(dynamicStylesAttr);
            console.log('Parsed dynamic styles:', dynamicStyles);
          } catch (e) {
            console.warn('Invalid dynamicStyles JSON:', e);
          }
        }
        
        const buttonText = buttonElement.textContent?.trim() || 'Try On';
        console.log('Button text:', buttonText);
        
        buttonData.push({
          element: buttonElement,
          skuId,
          skuCatalogName,
          dynamicStyles,
          buttonText
        });
      });
      
      // Clear the provider content and create a single React app
      providerElement.innerHTML = '';
      
      // Create error boundary component
      class ErrorBoundary extends React.Component {
        constructor(props) {
          super(props);
          this.state = { hasError: false, error: null };
        }
        
        static getDerivedStateFromError(error) {
          return { hasError: true, error: error };
        }
        
        componentDidCatch(error, errorInfo) {
          console.error('Aiuta SDK Error:', error, errorInfo);
        }
        
        render() {
          if (this.state.hasError) {
            return React.createElement('div', {
              style: { 
                padding: '10px', 
                border: '1px solid red', 
                backgroundColor: '#ffebee',
                color: '#c62828'
              }
            }, `Aiuta SDK Error: ${this.state.error?.message || 'Unknown error'}`);
          }
          
          return this.props.children;
        }
      }

      // Create React component that renders all buttons under one provider
      const AiutaApp = () => {
        try {
          console.log('Creating AiutaApp with API key:', apiKey);
          console.log('Button data:', buttonData);
          
          const buttons = buttonData.map((data, index) => {
            console.log(`Creating button ${index} with props:`, {
              skuId: data.skuId,
              skuCatalogName: data.skuCatalogName,
              dynamicStyles: data.dynamicStyles
            });
            
            return React.createElement(
              AiutaTryOnButton, 
              {
                key: index,
                skuId: data.skuId,
                skuCatalogName: data.skuCatalogName,
                dynamicStyles: data.dynamicStyles
              }, 
              data.buttonText
            );
          });
          
          console.log('Created buttons array:', buttons);
          
          return React.createElement(
            ErrorBoundary,
            null,
            React.createElement(
              AiutaTryOnSdkProvider, 
              { apiKey: apiKey }, 
              buttons
            )
          );
        } catch (error) {
          console.error('Error in AiutaApp:', error);
          return React.createElement('div', null, `Setup Error: ${error.message}`);
        }
      };

      // Mount the React component
      try {
        const root = createRoot(providerElement);
        root.render(React.createElement(AiutaApp));
        console.log(`Successfully mounted React app with ${buttonData.length} buttons`);
      } catch (error) {
        console.error('Error mounting React component:', error);
      }
    });
  } catch (error) {
    console.error('Error in initializeAiutaSDK:', error);
  }
}

console.log('Aiuta SDK wrapper loaded');